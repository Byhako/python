# XPath (XML Path Language)
https://devhints.io/xpath

XPath es a HTML, lo que las expresiones regulares son a texto.

https://toscrape.com/

```
$x('//h1/a/text()').map(i => i.wholeText

# Padres de span
$x('//span/..')

# Atributos, por ejemplo class de span
$x('//span/@class')
```

### Predicados en XPath
```
# Primer elemento
$x('/html/body/div/div[1]')

# Ultimo elemento
$x('/html/body/div/div[last()]')

# Todos los span que tienen class
$x('//span[@class]')

# Los span cuya clase es text
$x('//span[@class="text"]')

# Las 10 citas de nuestro sitio
$x('//span[@class="text"]/text()').map(i => i.data)
```

### Operadores
```
# span con clase distinta de text
$x('//span[@class!="text"]')

# los div con pasicion mayor a 1
$x('/html/body/div/div[position()>1]')

$x('//span[@class="text" and @class="tag-item"]')
$x('//span[@class="text" or @class="tag-item"]')

# Negando
$x('//span[not(@class="text")]')
```

### Wildcards o comodines.
No se exactamente el nodo que quiero, pero se aproximadamente donde se encuentra.

```
# Todo
$x('/*')

# Todo lo que html contiene
$x('/html/*')

# Todas las etiquedas ocn sus atributos
$x('//*')

# Todos los atributos de todos los span con class='text'
$x('//span[@class="text"]/@*')

# Todos los nodos que estan dentro de span con class='text' y itemprop='text'
$x('//span[@class="text" and @itemprop="text"]/node()')
```

### Buscando en el texto
```
# Todos los autores que comienzan con la letra A
$x('//small[@class="author" and starts-with(., "A")]/text()').map(i => i.data)

# Autores que contengan Ro
$x('//small[@class="author"and contains(., "Ro")]/text()').map(i => i.data)

# Solo funciona en la version 2, que no esta en los navegadores
$x('//small[@class="author"and ends-with(., "t")]/text()').map(i => i.data)

$x('//small[@class="author"and matches(., "A.*n")]/text()').map(i => i.data)
```
