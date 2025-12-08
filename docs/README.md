# A program for calculating the areas and perimeters of various figures

## circle.py
### Calculating the area and perimeter of a [circle](https://en.wikipedia.org/wiki/Circle)

### Area
#### Parameter:
`(float) r is the module of radius of the circle`

#### Return value:
`(float) the area of the circle`

### Perimeter
#### Parameter:
`(float) r is the module of radius of the circle`

#### Return value:
`(float) the perimeter of the circle`


#### Function call example: 
```
- print(area(int(input())))
- print(perimeter(int(input())))
```

## rectangle.py
### Calculating the area and perimeter of a [rectangle](https://en.wikipedia.org/wiki/Rectangle)

### Area
#### Parameter:
`(float) a is a module of height of the rectangle, (float) b is a module of width of the rectangle`

#### Return value:
`(float) the area of the rectangle`

### Perimeter
#### Parameter:
`(float) a is a module of height of the rectangle, (float) b is a module of width of the rectangle`

#### Return value:
`(float) the perimeter of the rectangle`


#### Function call example: 
```
- print(area(int(input()), int(input())))
- print(perimeter(int(input()), int(input())))
```

## square.py
### Calculating the area and perimeter of a [square](https://en.wikipedia.org/wiki/Square)

### Area
#### Parameter:
`(float) a is a module of side of the square`

#### Return value:
`(float) the area of the square`

### Perimeter
#### Parameter:
`(float) a is a module of side of the square`

#### Return value:
`(float) the perimeter of the square`


#### Function call example: 
```
- print(area(int(input())))
- print(perimeter(int(input())))
```

## triangle.py
### Calculating the area and perimeter of a [triangle](https://en.wikipedia.org/wiki/Triangle)


### Area
#### Parameter:
`(float) a is module of a side, (float) h is a module of height that lowered to side A`

#### Return value:
`(float) the area of the square`

### Perimeter
#### Parameter:
`(float) a is a module of side, (float) b is a module of side, (float) c is a module of side`

#### Return value:
`(float) the perimeter of the square`


#### Function call example: 
```
- print(area(int(input()), int(input())))
- print(perimeter(int(input()), int(input()), int(input())))
```


## Math formulas

### [Area](https://en.wikipedia.org/wiki/Area)
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ah/2

### [Perimeter](https://en.wikipedia.org/wiki/Perimeter)
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c


## Testing
The project includes a complete set of unit tests for all functions. All tests are located in the tests folder.

### Running all the tests
``` python -m unittest discover -s tests -p "test_*.py" -v ```

### Test structure and launch method
test_rectangle.py: 8 tests for rectangle

``` python -m unittest tests.test_rectangle -v ```

--------------------------------------------------------------------
test_square.py: 9 tests for square

``` python -m unittest tests.test_square -v ```

--------------------------------------------------------------------

test_triangle.py: 12 tests for triangle

``` python -m unittest tests.test_triangle -v ```

--------------------------------------------------------------------

test_circle.py: 11 tests for circle

``` python -m unittest tests.test_circle -v ```


## Test coverage

Normal use cases

Boundary cases (zero values)

Negative values

Floating point numbers

Error handling (incorrect data types)

## Documentation

All documentation is in docs and was compiled using [pdoc](https://pdoc.dev/)

## Project change history with commit hashes

#### dc5e59eaaf45d0cb8ed0e00d3f5cfe0127664c09
#### bfa73b81cd4b82ea7a614e2f77acceb718cdee5b
#### d078c8d9ee6155f3cb0e577d28d337b791de28e2
#### 8ba9aeb3cea847b63a91ac378a2a6db758682460


## MIT License