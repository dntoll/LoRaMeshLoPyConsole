# micropythonconsole


Code to frame and a title
```python

  from lib.Console import Console
  
  c = Console(height= 6)
  c.frame(0,0, 15, 3)
  c.printAt("Sin", x=6, y=1, color="Blue", background="Black")
  c.show()
```


Creating and updating values 
```python
  from lib.Console import Console

  c = Console(height= 6)
  value = c.createValue("Sin", "m", decimals=2, x=2, y=2, color="Green", background="Black", detail=1)
  value.set(sensorValue)
  c.show()
```
