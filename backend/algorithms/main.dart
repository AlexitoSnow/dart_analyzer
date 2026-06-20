/**
 * Prueba de código Grupal
 * Snippet conjunto que integra todas las posibilidades y reglas léxicas 
 * de Alexander, Sofía y Daniel.
*/
void main() {
  // Sofia: variables, constantes, int, Map, asignación, estructuras de control, print
  var variable = 100;
  final int miEntero = 50;
  const bool flag = true;
  Map<String, int>? mapa;
  
  // Daniel: double, bool, Set, nulabilidad, operadores lógicos y relacionales, operador flecha
  double decimal = 3.14;
  bool esFalso = false;
  Set<double>? conjunto;
  int? numeroNulable = null;
  bool condicion = (decimal >= 3.0) && (decimal <= 4.0) || !esFalso;
  int obtenerValor() => 10;
  
  // Alexander: String, List, null, operadores aritméticos, relacionales < >, strings y delimitadores
  String cadenaDoble = "Texto en comillas dobles";
  String cadenaSimple = 'Texto en comillas simples';
  List<int> miLista = [1, 2, 3];
  var nulo = null;
  int calculo = (10 + 5) * 2 / 3 - 1 % 2;
  variable++;
  variable--;
  
  if (variable < 200) {
    // menor
  }
  if (variable > 50) {
    // mayor
  }
  
  switch (variable) {
    case 100:
      print(cadenaDoble);
      break;
    default:
      print(cadenaSimple);
      break;
  }
  
  for (int i = 0; i < 5; i++) {
    while (variable > 90) {
      break;
    }
  }
  
  return;
}

class ParentClass {
  int method() {}
}

// 'extends' no esta en las keywords, se espera que se lea como ID
class SonClass extends ParentClass {
  // '@override' no esta en las keywords, se espera que 'override' se lea como ID
  // y que '@' se lea como un error intencional para probar los casos de error
  @override
  int method() {}
}