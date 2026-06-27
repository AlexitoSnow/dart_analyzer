/**
 * Prueba de código Grupal - main.dart
 * Snippet conjunto que integra todas las posibilidades y reglas léxicas 
 * de Alexander, Sofía y Daniel, incluyendo estructuras faltantes y 
 * errores intencionales para la validación final del compilador.
*/
void main() {
  // ==========================================
  // --- ESTRUCTURAS DE SOFIA IZAGUIRRE ---
  // ==========================================
  var variable = 100;
  final int miEntero = 50;
  const bool flag = true;
  
  // Estructura Map (Vacía, Nulable e Inicializada con valores)
  Map<String, int>? mapaNulable;
  Map<String, int> edades = {'Juan': 25, 'Ana': 30};

  if (variable < 200) {
    print(variable);
  } else {
    print(flag);
  }

  // ❌ ERROR SINTÁCTICO INTENCIONAL (Sofia): Falta paréntesis en la condición del if.
  // Yacc arrojará: "Error Sintactico: Estructura no valida cerca de 'variable'"
  if variable > 50 {
    print("Error");
  }


  // ==========================================
  // --- ESTRUCTURAS DE DANIEL CORTEZ ---
  // ==========================================
  double decimal = 3.14;
  bool esFalso = false;
  int? numeroNulable = null;
  
  // Estructura Set (Nulable e Inicializada con valores)
  Set<double>? conjuntoNulable;
  Set<double> temperaturas = {36.5, 37.0, 38.2};
  
  bool condicion = (decimal >= 3.0) && (decimal <= 4.0) || !esFalso;
  int obtenerValor() => 10;
  
  // Input/Output (Faltante en el código original)
  String? entrada = stdin.readLineSync();

  while (decimal < 5.0) {
    decimal++;
    break;
  }

  // ❌ ERROR SINTÁCTICO INTENCIONAL (Daniel): Función lambda sin valor a retornar.
  // Yacc arrojará: "Error Sintactico: Estructura no valida cerca de ';'"
  bool funcionIncompleta() => ;


  // ==========================================
  // --- ESTRUCTURAS DE ALEXANDER NIEVES ---
  // ==========================================
  String cadenaDoble = "Texto en comillas dobles";
  String cadenaSimple = 'Texto en comillas simples';
  List<int> miLista = [1, 2, 3];
  var nulo = null;
  
  int calculo = (10 + 5) * 2 / 3 - 1 % 2;
  variable++;
  variable--;

  switch (variable) {
    case 100:
      print(cadenaDoble);
      break;
    default:
      print(cadenaSimple);
      break;
  }
  
  for (int i = 0; i < 5; i++) {
    print(i);
  }

  // ❌ ERROR LÉXICO INTENCIONAL: El símbolo '~' no pertenece al alfabeto de Dart definido.
  // Lex arrojará: "Caracter ilegal: '~' en la linea 68" y continuará compilando.
  int operacionInvalida = 5 ~ 3;

  return;
}

// Declaración de Clases y Funciones Void (Alexander)
class ParentClass {
  int method() {}
}

// 'extends' se leerá correctamente como un ID al no estar en el diccionario keywords.
class SonClass extends ParentClass {
  
  // ❌ ERROR LÉXICO INTENCIONAL: '@' no está en el alfabeto.
  // Lex arrojará: "Caracter ilegal: '@'". Luego, Yacc leerá 'override' como un decorador ID normal.
  @override
  int method() {}
}