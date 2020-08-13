
from scipy import matmul, rand, loadtxt

from time import perf_counter
import matplotlib.pyplot as plt

tiempo = []
memoria = []
N = [1,2,5,10,12,15,20,25,30,40,45,50,60,100,200,500,1000,2000,5000]#,10000,20000]
Ncorridas = 10

for i in range(Ncorridas):
    archivo = (f"matmul{i}.txt")
    file = open(archivo,"w")
    
    for n in N:
        A = rand(n,n)
        B = rand(n,n)
        t1 = perf_counter()
        C = A@B        
        t2 = perf_counter()
        dt = t2 - t1 #tiempo que tarda
        mem = 3*(n**2)*8

        tiempo.append(dt)
        memoria.append(mem)
        
        #print (f"el tiempo es = {dt}")
        #print (f"la memoria es = {mem}")
        file.write(f"{n} {dt} {mem}\n")
        file.flush()
    file.close()
    
    from scipy import matmul, rand, loadtxt

from time import perf_counter
import matplotlib.pyplot as plt

Ncorridas = 10

plt.figure()
x = [10,20,50,100,200,500,1000,2000,5000,10000,20000]
xlab = ["10","20","50","100","200","500","1000","2000","5000","10000","20000"]
y = [0.1e-3,1e-3,1e-2,0.1,1.,10.,60,60*10, 60*100]
ylab = ["0.1 ms","1 ms","10 ms","0.1 s","1 s","10 s","1 min","10 min"] 
y2 = [10**3,10**4,10**5,10**6,10**7,10**8,10**9,10**10]
ylab2 = ["1 KB","10 KB","100 KB","1 MB","10 MB","100 MB","1 GB","10 GB","100 GB"]
limite1 = [0.1e-4,20000,1e-2,6000]
limite2 = [0.1e-4,20000,1e-2,10000000000]
#tiempo
plt.title("Rendimiento A@B")
for i in range(Ncorridas):
    archivo1 = f"matmul{i}.txt"
    datos = loadtxt(archivo1)
    tiempo_lista = datos[:,1]
    n_lista= datos[:,0]
    mem_lista = datos[:,2]      
    plt.subplot(2,1,1)
    plt.title("Rendimiento A@B")
    plt.loglog (n_lista,tiempo_lista,"-o")  
    plt.xticks(x,[])
    plt.yticks(y,ylab)
    plt.grid(True) 
    plt.ylabel("Tiempo Transcurrido")

plt.subplot(2,1,2)
plt.loglog(n_lista,mem_lista,"-o")  
plt.xticks(x,xlab,rotation=45)
plt.yticks(y2,ylab2)
plt.grid(True) 
plt.ylabel("Uso Memoria")
plt.xlabel("Tamaño de la matriz")

plt.axhline(4e9)
plt.tight_layout()
plt.savefig("grafico.png")
plt.show()
