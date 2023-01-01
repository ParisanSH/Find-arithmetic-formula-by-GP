import random
import math

target = {}
for x in range (-100 , 100):
    # you could update this line to get any formulas
    target[x] = x*x + 2*x + 1   

D_max = 2
terminal_set = ['x' ,1,2,3,4,5,6,7,8,9]
function_set = ['+','-', '*', '/']
pop = dict()
class node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.father = None
        if data in terminal_set:
            self.types = 1
        else:
            self.types = 0

def inorder(obj): 
    if obj is not None: 
        inorder(obj.left) 
        print (obj.data,end =" ")
        inorder(obj.right)

def instruct(model, d_max, current_d,terminal, func):
    flag = random.randint(0,1)
    if flag == 0 or model == 'f':
        val = func[random.randint(0,3)]
        root = node(val)
        root.father = None            
        root.right= instruct_helper(model, d_max, current_d+1,root,terminal, func)
        root.left= instruct_helper(model, d_max, current_d+1,root,terminal, func)
    if flag ==1 and model == 'g':
        val = terminal[random.randint(0,9)]
        root = node(val)            
    return root
   
def instruct_helper(model, d_max, current_d,father,terminal, func):
        val = 0
        if current_d < d_max -1:
            if model == 'f':
                    val = func[random.randint(0,3)]
                    obj = node(val)            
                    obj.right= instruct_helper(model, d_max, current_d+1,obj,terminal, func)
                    obj.left= instruct_helper(model, d_max, current_d+1,obj,terminal, func)
                #    print(model, current_d,father.data,val)

            else:
                flag = random.randint(0,1)
                if flag == 0:
                    val = func[random.randint(0,3)]
                    obj = node(val)            
                    obj.right= instruct_helper(model, d_max, current_d+1,obj,terminal, func)
                    obj.left= instruct_helper(model, d_max, current_d+1,obj,terminal, func)
                else:
                    val = terminal[random.randint(0,9)]
                    obj = node(val)
        else:
            val = terminal[random.randint(0,9)]
            obj = node(val)
        obj.father = father
        return obj

def cut(chorom):
    #bfs based
    print("\n")
    queue = [] 
    queue.append(chorom) 
    while queue: 
        #entekhab
        s = queue.pop()
        prob = random.uniform(0,1)
        if prob < .2:
            return s
        else:
            #bast
            if s.right != None:
                queue.append(s.right) 
            if s.left != None:
                queue.append(s.left)
    return s
                
def swap(node1, node2):
    #print("swaping ", node1.data, node2.data)
    n1_prime = node(node1.data)
    n1_prime.left = node1.left
    n1_prime.right = node1.right
    n1_prime.father = node2.father

    n2_prime = node(node2.data)
    n2_prime.left = node2.left
    n2_prime.right = node2.right
    n2_prime.father = node1.father
                
    if node1.father == None and node2.father == None:
        node1.data = n2_prime.data
        node1.right = n2_prime.right
        node1.left = n2_prime.left

        node2.data = n1_prime.data
        node2.right = n2_prime.right
        node2.left = n2_prime.left
        
    elif node1.father == None and node2.father != None:
        if node2.father.left == node2:
            node2.father.left = n1_prime
        elif node2.father.right == node2:
            node2.father.right = n1_prime
                
        node1.data = n2_prime.data
        node1.right = n2_prime.right
        node1.left = n2_prime.left

    elif node1.father != None and node2.father == None:
        if node1.father.left == node1:
            node1.father.left = n2_prime
        elif node1.father.right == node1:
            node1.father.right = n2_prime
                
        node2.data = n1_prime.data
        node2.right = n2_prime.right
        node2.left = n2_prime.left
    
    else:
        if node2.father.left == node2:
            node2.father.left = n1_prime
        elif node2.father.right == node2:
            node2.father.right = n1_prime
      
        if node1.father.left == node1:
            node1.father.left = n2_prime
        elif node1.father.right == node1:
            node1.father.right = n2_prime
    
    
def crossover(chorom1 , chorom2):
    #global terminal_set
    node1= cut(chorom1)
    node2= cut(chorom2)
    #print("type(node1)", type(node1))
    #print("type(node2)", type(node2))
    swap(node1, node2)
    return 

def initialisation(d , terminal , func):
    #grow initialise 
    num = 500 #population size
    for i in range(1,num+1):
        if i < num/2:
            pop[i] = instruct('g',d,0,terminal, func)
        else:
            #full initialais
            pop[i] = instruct('f',d,0,terminal, func)
    for this in list(pop.keys()):
        print("\n", this,":" , end= " ")
        inorder(pop[this])
    #----------------------------------------------------------
    """crossover(pop[1], pop[2])
    print("--------- after cross over ----------")
    inorder(pop[1])
    print("\n")
    inorder(pop[2])"""

def mutation(chorom):

    new_random_tree = 0
    p_full = random.uniform(0,1)

    if p_full < 0.5: # make new random grow_tree
        new_random_tree = instruct('g',D_max,0,terminal_set, function_set)
    else:
        new_random_tree = instruct('f',D_max,0,terminal_set, function_set)
    crossover(chorom , new_random_tree )
    return chorom

def evaluateExpressionTree(root , current_x): 
  
    # empty tree 
    if root is None: 
        return 0
  
    # leaf node 
    if root.left is None and root.right is None and root.data != 'x': 
        return int(root.data) 
    if root.left is None and root.right is None and root.data == 'x':
        return int(current_x)
    # evaluate left tree 
    left_sum = evaluateExpressionTree(root.left , current_x) 
  
    # evaluate right tree 
    right_sum = evaluateExpressionTree(root.right , current_x) 
  
    # check which operation to apply 
    if root.data == '+': 
        return left_sum + right_sum 
      
    elif root.data == '-': 
        return left_sum - right_sum 
      
    elif root.data == '*': 
        return left_sum * right_sum 
      
    else: 
        return left_sum / (right_sum + 0.000000001)
        
def fitness_func(key):
    this_chorom = pop[key]
    fit = list()
    i = 0
    inorder(this_chorom)
    for x in range (-100 , 100):
        fitness =evaluateExpressionTree(this_chorom , x)
        fit.append(fitness)
        fit[i] = math.pow((fit[i] - target[x]) , 2)
        i += 1
    
    fitness = sum(fit)/len(fit)
    fitness = fitness * (-1)
    return(fitness)

def selection():
    #tournoment size  = 8
    selected = random.randint(1,500)
    for i in range(7):
        j = random.randint(1,500)
        if fitness_func(selected) < fitness_func(j):
            selected = j
    return int(selected)

initialisation(D_max , terminal_set , function_set )
generation_number = 1

while (generation_number < 30):
    new_pop = dict()
    curent_fitness = dict()
    i= 500
    j= 1 
    while i > 0 :

        chorom1 = pop[selection()]
        chorom2 = pop[selection()]
        print("\n",i,':')
        #crossover or mutatio
        p_crossover = random.uniform(0,1)
        
        if p_crossover > .2: # do crossover
            crossover(chorom1 , chorom2)
            new_pop[j] = chorom1
            new_pop[j+1]= chorom2
        else:   #do mutate
            new_pop[j] = mutation(chorom1)
            new_pop[j+1] = mutation (chorom2)
        j += 2
        i -= 1

    for chorom in list(pop.keys()):
        curent_fitness[chorom] = fitness_func(chorom)
        if curent_fitness[chorom] == 0:
            print("\n")
            inorder(pop[chorom])
    pop = dict()
    pop = new_pop
    

