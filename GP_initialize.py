import random
import math


target = {}
for x in range (-100 , 100):
    target[x] = x*x + 2*x + 1   # you could update this line to get any formulas


#main
D_max = 2
terminal_set = ['x' ,1,2,3,4,5,6,7,8,9]
function_set = ['+','-', '*', '/']

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
        #print(s.data, "###########", type(s)) 
        #test
        prob = random.uniform(0,1)
        if prob < .2:
            return s
        else:
            #bast
            if s.right != None:
                queue.append(s.right) 
            if s.left != None:
                queue.append(s.left) 
def swap(node1, node2):       
    if node1.father == None and node2.father == none:
        node1 , node2 = node2 , node1
    if node1.father == None and node2.father != none:
        node2.father.left = node1
        node2.father=none
        
    if node1 root bood node 2 nabud
    if avali root bud dovomi nabud
    if hichkodoom root nabud

def crossover(chorom1 , chorom2):
    #global terminal_set
    node1= cut(chorom1)
    node2= cut(chorom2)
    swap(node1, node2)
    return 

def initialisation(d , terminal , func):
    pop = dict()
    #grow initialise 
    num = 4
    for i in range(1,num):
        if i < num/2:
            pop[i] = instruct('g',d,0,terminal, func)
        else:
            #full initialais
            pop[i] = instruct('f',d,0,terminal, func)
    for this in list(pop.keys()):
        print("\n", this,":" , end= " ")
        inorder(pop[this])
    crossover(pop[1], pop[2])
    print("--------- after cross over ----------")
    print("\n", pop[1],":" , end= " ")
    print("\n", pop[2],":" , end= " ")
  

initialisation(D_max , terminal_set , function_set )

