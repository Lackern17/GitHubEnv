# GitHubEnv
Pasos a seguir para crear un entorno "conda" y exportarlo a Git:

1- Crear un repositorio Git y clonarlo a local
  
2- Crear un nuevo entorno en conda y activalo.</br>  
    <code> conda create --name "nombre" </code><br>  
    <code> conda activate "nombre"</code><br>  
        
Luego instalaremos las bibliotecas que necesitemos, en este caso 3:<br>  
        <code> conda install numpy  </code><br>  
        <code> conda install pandas </code><br>  
        <code> conda install matplotlib </code><br>  
        
Una vez que tenemos todo nuestro entorno preparado, procedemos a escribir a nuestro codigo.<br>  
        <code> nano codeytest.py </code><br>  
        <code> python3 codetest.py </code><br>  
        
Tras escribirlo y comprobar que funciona podemos proceder a subirlo, pero primero exportaremos y subiremos el entorno.

<code> conda env export > configGitHubEnv.yml </code>

Por ultimo Git para subirlo todo.  

<code> Git add *</code> <code>Git commit -m "nombre del commit" </code> <code>Git push</code>
        
    
