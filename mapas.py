import json

class Mapa: 
    mapa1 = {
        'a1':{'b1':1, 'a2':1},
        'a2':{'a1':1, 'a3':1},
        'a3':{'a2':1, 'a4':2},
        'a4':{'a3':1, 'b4':2},
        'b1':{'c1':1, 'a1':1},
        'b4':{'c4':2, 'a4':2},
        'c1':{'d1':1, 'b1':1},
        'c4':{'d4':1, 'b4':2},
        'd1':{'d2':1, 'c1':1},
        'd2':{'d1':1, 'd3':1},
        'd3':{'d2':1, 'd4':1},
        'd4':{'d3':1, 'c4':2}
    }
    
    mapa1Texturas ="""
            1111
            1002
            1002
            1112
            """
    
    mapa2 = {
        'a1':{'b1':1, 'a2':1},
        'a2':{'a1':1, 'a3':1},
        'a3':{'a2':1, 'a4':2},
        'a4':{'a3':1, 'b4':2},
        'a6':{'b6':1},
        'b1':{'c1':1, 'a1':1},
        'b4':{'c4':1, 'a4':2},
        'b6':{'c6':2, 'a6':1},
        'c1':{'b1':1, 'c2':1},
        'c2':{'c1':1, 'c3':1, 'd2':1},
        'c3':{'c2':1, 'c4':1},
        'c4':{'c3':1, 'b4':2, 'c5':2},
        'c5':{'c4':1, 'c6':2},
        'c6':{'c5':2, 'b6':1, 'd6':2},
        'd2':{'e2':1, 'c2':1},
        'd6':{'e6':1, 'c6':2},
        'e1':{'e2':1},
        'e2':{'e1':1, 'd2':1, 'f2':1},
        'e4':{'f4':1, 'e5':1},
        'e5':{'e4':1, 'e6':1},
        'e6':{'f6':1, 'd6':2},
        'f2':{'f3':1, 'e2':1},
        'f3':{'f2':1, 'f4':1},
        'f4':{'f3':1, 'e4':1},        
        'f6':{'e6':1}
    }
    
    mapa2Texturas ="""
            011101
            110111
            010002
            111122
            100201
            111201
            """

    mapa3 = {
        'a1':{'b1':1, 'a2':1},
        'a2':{'a1':1, 'a3':1, 'b2':3},
        'a3':{'a2':1, 'a4':1},
        'a4':{'a3':1, 'a5':1},
        'a5':{'a4':1, 'a6':3, 'b5':1},
        'a6':{'a5':1, 'a7':3, 'b6':2},
        'a7':{'a6':3, 'a8':3},
        'a8':{'a7':3, 'a9':3},
        'a9':{'a8':3, 'a10':1},
        'a10':{'a9':3, 'b10':1},
        'b1':{'c1':1, 'a1':1, 'b2':3},
        'b2':{'b1':1, 'c2':3, 'a2':1},
        'b5':{'a5':1, 'b6':2},
        'b6':{'b5':1, 'a6':3, 'c6':2},
        'b9':{'c9':1, 'a9':3, 'b10':1},
        'b10':{'b9':1, 'a10':1},
        'c1':{'d1':2, 'b1':1, 'c2':3},
        'c2':{'d2':3, 'b2':3, 'c3':1},
        'c3':{'c2':3, 'c4':1},
        'c4':{'c3':1, 'd4':1},
        'c6':{'d6':2, 'b6':2},
        'c9':{'d9':1, 'b9':1},
        'd1':{'e1':2, 'c1':1, 'd2':2},
        'd2':{'d1':2, 'b2':3},
        'd4':{'e4':1, 'c4':1},
        'd6':{'c6':2, 'd7':2},
        'd7':{'d6':2, 'e7':2},
        'd9':{'e9':1, 'c9':1},
        'e1':{'f1':2, 'd1':2},
        'e4':{'f4':1, 'd4':1},
        'e7':{'d7':2, 'e8':1},
        'e8':{'e7':2, 'e9':1, 'f8':1},
        'e9':{'e8':1, 'f9':1, 'd9':1},
        'f1':{'g1':1, 'e1':2, 'f2':1},
        'f2':{'f1':2, 'f3':1},
        'f3':{'f2':1, 'g3':1, 'f4':1},
        'f4':{'f3':1, 'g4':3, 'e4':1},
        'f6':{'g6':3},
        'f8':{'g8':1, 'e8':1, 'f9':1},
        'f9':{'f8':1, 'e9':1, 'f10':2},
        'f10':{'f9':1, 'g10':2},
        'g1':{'h1':1, 'f1':2},
        'g3':{'f3':1, 'g4':3},
        'g4':{'g3':1, 'f4':1, 'g5':3},
        'g5':{'g4':3, 'h5':1, 'g6':3},
        'g6':{'g5':3, 'f6':1, 'g7':1},
        'g7':{'g6':3, 'h7':1, 'g8':1},
        'g8':{'g7':1, 'h8':3},
        'g10':{'h10':2, 'f10':2},
        'h1':{'i1':1, 'g1':1, 'h2':1},
        'h2':{'h1':1, 'i2':3},
        'h5':{'i5':3, 'g5':3},
        'h7':{'h8':3, 'g7':1},
        'h8':{'h7':1, 'g8':1},
        'h10':{'i10':2, 'g10':2},
        'i1':{'j1':1, 'h1':1, 'i2':3},
        'i2':{'i1':1, 'i3':3, 'h2':1},
        'i3':{'i2':3, 'i4':3},
        'i4':{'i3':3, 'i5':3, 'j4':1},
        'i5':{'i4':3, 'i6':1, 'j5':1, 'h5':1},
        'i6':{'j6':1, 'i5':3},
        'i10':{'j10':1, 'h10':2},
        'j1':{'i1':1},
        'j4':{'i4':3, 'j5':1},
        'j5':{'j4':1, 'j6':1, 'i5':3},
        'j6':{'j5':1, 'j7':1, 'i6':1},
        'j7':{'j6':1, 'j8':1},
        'j8':{'j7':1, 'j9':1},
        'j9':{'j8':1, 'j10':1},
        'j10':{'j9':1, 'i10':2}
    }
    
    mapa3Texturas ="""
            1001111111
            1333310002
            1100101302
            1013331102
            2111010112
            2001002110
            2301022010
            1311020010
            1300120011
            1111133331
            """
    
    
    NuevoMapa = {
        'a2':{'a3':1, 'b2':3},
        'a3':{'a2':1, 'b3':1},
        'a5':{'a6':2, 'b5':2},
	    'a6':{'a5':2, 'b6':2},
        'a8':{'a9':1, 'b8':1},
        'a9':{'a8':1, 'b9':3},
        'b1':{'c1':1, 'b2':3},
        'b2':{'b1':1, 'b3':1, 'a2':1, 'c2':1},
        'b3':{'b2':3, 'b4':1, 'a3':1},
        'b4':{'b3':1, 'b5':2, 'c4':2},
        'b5':{'b4':1, 'b6':2, 'a5':2, 'c5':3},
        'b6':{'b5':2, 'a6':2, 'c6':3, 'b7':1},
        'b7':{'b6':2, 'b8':1, 'c7':2},
        'b8':{'b7':1, 'b9':3, 'a8':1},
        'b9':{'b8':1, 'b10':1, 'c9':1},
        'b10':{'b9':3, 'c10':1},
        'c1':{'d1':1, 'b1':1, 'c2':1},
        'c2':{'d2':1, 'b2':3, 'c1':1},
        'c4':{'c5':3, 'd4':1, 'b4':1},
        'c5':{'c6':3, 'd5':3, 'c4':2, 'b5':2},
        'c6':{'c5':3, 'c7':2, 'd6':3, 'b6':2},
        'c7':{'c6':3, 'd7':1, 'b7':1},
        'c9':{'c10':1, 'd9':1, 'b9':3},
        'c10':{'d10':1, 'c9':1, 'b10':1},
        'd1':{'c1':1, 'd2':1},
        'd2':{'d1':1, 'c2':1, 'd3':2, 'e2':2},
        'd3':{'d2':1, 'd4':1, 'e3':3},
        'd4':{'d3':2, 'd5':3, 'e4':3, 'c4':2},
        'd5':{'d4':1, 'd6':3, 'c5':3},
        'd6':{'d5':3, 'd7':1, 'c6':3},
        'd7':{'d6':3, 'd8':2, 'e7':3, 'c7':2},
        'd8':{'d7':1, 'd9':1, 'e8':3},
        'd9':{'d8':2, 'd10':1, 'e9':2, 'c9':1},
        'd10':{'c10':1, 'd9':1},
        'e2':{'f2':2, 'e3':3, 'd2':1},
        'e3':{'e2':2, 'e4':3, 'f3':3, 'd3':2},
        'e4':{'e3':3, 'f4':3, 'd4':1},
        'e7':{'f7':3, 'd7':1, 'e8':3},
        'e8':{'e7':3, 'f8':3, 'e9':2, 'd8':2},
        'e9':{'e8':3, 'f9':2, 'd9':1},
        'f2':{'g2':1, 'f3':3, 'e2':2},
        'f3':{'f2':2, 'f4':3, 'e3':3, 'g3':2},
        'f4':{'f3':3, 'g4':1, 'e4':3},
	    'f7':{'g7':1, 'e7':3, 'f8':3},
	    'f8':{'f7':3, 'g8':2, 'f9':2, 'e8':3},       
	    'f9':{'f8':3, 'g9':1, 'e9':2},
        'g1':{'h1':1, 'g2':1},
        'g2':{'g1':1, 'f2':2, 'g3':2, 'h2':1},
        'g3':{'g2':1, 'g4':1, 'f3':3},
        'g4':{'g3':2, 'g5':3, 'h4':2, 'f4':3},
        'g5':{'g4':1, 'g6':3, 'h5':3},
        'g6':{'g5':3, 'g7':1, 'h6':3},
        'g7':{'g6':3, 'g8':2, 'f7':3, 'h7':2},
        'g8':{'g7':1, 'g9':1, 'f8':3},
        'g9':{'g8':2, 'g10':1, 'f9':2, 'h9':1},
        'g10':{'h10':1, 'g9':1},
        'h1':{'i1':1, 'g1':1, 'h2':1},
        'h2':{'g2':1, 'i2':3, 'h1':1},
        'h4':{'h5':3, 'i4':1, 'g4':1},
        'h5':{'h6':3, 'g5':3, 'h4':2, 'g5':3},
        'h6':{'h5':3, 'h7':2, 'g6':3, 'i6':2},
        'h7':{'h6':3, 'i7':1, 'g7':1},
        'h9':{'h10':1, 'g9':1, 'i9':3},
        'h10':{'g10':1, 'h9':1, 'i10':1},
        'i1':{'h1':1, 'i2':3},
        'i2':{'i1':1, 'i3':1, 'h2':1, 'j2':1},
        'i3':{'i2':3, 'i4':1, 'j3':1},
        'i4':{'i3':1, 'i5':2, 'h4':2},
        'i5':{'i4':1, 'i6':2, 'j5':2, 'h5':3},
        'i6':{'i5':2, 'h6':3, 'j6':2, 'i7':1},
        'i7':{'i6':2, 'i8':1, 'h7':2},
        'i8':{'i7':1, 'i9':3, 'j8':1},
        'i9':{'i8':1, 'i10':1, 'j9':1},
        'i10':{'i9':3, 'h10':1},
	    'j2':{'j3':1, 'i2':3},
        'j3':{'j2':1, 'i3':1},
        'j5':{'j6':2, 'i5':2},
	    'j6':{'j5':2, 'i6':2},
        'j8':{'j9':1, 'i8':1},
        'j9':{'j8':1, 'i9':3}
    }
    
    mapaNuevoTexturas ="""
            0110220110
            1311221131
            1102332011
            1121331211
            0233003320
            0233003320
            1121331211
            1102332011
            1311221131
            0110220110
            """

    MapaSinSolucion = {
        'j1': {'j2': 2, 'i1': 3},
        'j2': {'j1': 1, 'j3': 2, 'i2': 2},
        'j3': {'j2': 2, 'j4': 3, 'i3': 3},
        'j4': {'j3': 2, 'j5': 1, 'i4': 2},
        'j5': {'j4': 3, 'i5': 2},
        'j9': {'j10': 2},
        'j10': {'j9': 3, 'i10': 1},
        'i1': {'j1': 1, 'i2': 2, 'h1': 1},
        'i2': {'j2': 2, 'i1': 3, 'i3': 3, 'h2': 3},
        'i3': {'j3': 2, 'i2': 2, 'i4': 2, 'h3': 1},
        'i4': {'j4': 3, 'i3': 3, 'i5': 2, 'h4': 2},
        'i5': {'j5': 1, 'i4': 2, 'i6': 2, 'h5': 3},
        'i6': {'i5': 2, 'i7': 3, 'h6': 2},
        'i7': {'i6': 2, 'i8': 2, 'h7': 1},
        'i8': {'i7': 3, 'h8': 2},
        'i10': {'j10': 2, 'h10': 1},
        'h1': {'i1': 3, 'h2': 3},
        'h2': {'i2': 2, 'h1': 1, 'h3': 1},
        'h3': {'i3': 3, 'h2': 3, 'h4': 2, 'g3': 2},
        'h4': {'i4': 2, 'h3': 1, 'h5': 3, 'g4': 3},
        'h5': {'i5': 2, 'h4': 2, 'h6': 2, 'g5': 2},
        'h6': {'i6': 2, 'h5': 3, 'h7': 1, 'g6': 2},
        'h7': {'i7': 3, 'h6': 2, 'h8': 2, 'g7': 3},
        'h8': {'i8': 2, 'h7': 1, 'g8': 3},
        'h10': {'i10': 1, 'g10': 2},
        'g3': {'h3': 1, 'g4': 3, 'f3': 1},
        'g4': {'h4': 2, 'g3': 2, 'g5': 2, 'f4': 3},
        'g5': {'h5': 3, 'g4': 3, 'g6': 2},
        'g6': {'h6': 2, 'g5': 2, 'g7': 3, 'f6': 2},
        'g7': {'h7': 1, 'g6': 2, 'g8': 3},
        'g8': {'h8': 2, 'g7': 3, 'g9': 2},
        'g9': {'g8': 3, 'g10': 2, 'f9': 1},
        'g10': {'h10': 1, 'g9': 2, 'f10': 2},
        'f1': {'f2': 1, 'e1': 3},
        'f2': {'f1': 1, 'f3': 1, 'e2': 3},
        'f3': {'g3': 2, 'f2': 1, 'f4': 3},
        'f4': {'g4': 3, 'f3': 1, 'e4': 3},
        'f6': {'g6': 2},
        'f9': {'g9': 2, 'f10': 2, 'e9': 3},
        'f10': {'g10': 2, 'f9': 1, 'e10': 3},
        'e1': {'f1': 1, 'e2': 3, 'd1': 1},
        'e2': {'f2': 1, 'e1': 3},
        'e4': {'f4': 3, 'd4': 3},
        'e7': {'e8': 3, 'd7': 3},
        'e8': {'e7': 3, 'e9': 3, 'd8': 2},
        'e9': {'f9': 1, 'e8': 3, 'e10': 3, 'd9': 3},
        'e10': {'f10': 2, 'e9': 3, 'd10': 2},
        'd1': {'e1': 3, 'c1': 1},
        'd3': {'d4': 3},
        'd4': {'e4': 3, 'd3': 2},
        'd6': {'d7': 3, 'c6': 2},
        'd7': {'e7': 3, 'd6': 3, 'd8': 2},
        'd8': {'e8': 3, 'd7': 3, 'd9': 3, 'c8': 2},
        'd9': {'e9': 3, 'd8': 2, 'd10': 2, 'c9': 1},
        'd10': {'e10': 3, 'd9': 3},
        'c1': {'d1': 1, 'c2': 2, 'b1': 2},
        'c2': {'c1': 1},
        'c6': {'d6': 3},
        'c8': {'d8': 2, 'c9': 1},
        'c9': {'d9': 3, 'c8': 2, 'b9': 2},
        'b1': {'c1': 1},
        'b3': {'b4': 1, 'a3': 3},
        'b4': {'b3': 3, 'b5': 2},
        'b5': {'b4': 1, 'a5': 1},
        'b7': {'a7': 3},
        'b9': {'c9': 1, 'b10': 1, 'a9': 3},
        'b10': {'b9': 2},
        'a2': {'a3': 3},
        'a3': {'b3': 3, 'a2': 2},
        'a5': {'b5': 2},
        'a7': {'b7': 2},
        'a9': {'b9': 2}
    }
    
    mapaSinSolucionTexturas ="""
            1223100032
            3232223201
            1312321201
            0023223322
            1113020012
            3303003333
            1023033232
            1200020210
            2031202021
            0230103030
            """
    
        
    
    f= open('Mapa_prueba.json')
    mapaPrueba = json.load(f)
#==========================================================================================
'''
object = Mapa()
prueba = object.mapaPrueba
print(prueba)
'''
