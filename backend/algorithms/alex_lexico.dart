/**
 * Prueba de código para Alexander Nieves
 * Snippet de prueba para las reglas y tokens implementados por Alexander Nieves
 * (class, String, List, case, default, null, operadores aritméticos, <, >, cadenas 
 * de texto y delimitadores).
*/
void main() {
  String mensaje = "Hola Mundo";
  final mensaje2 = 'Hola de nuevo';
  List<int> lista = [1, 2, 3];
  var valorNulo? = null;
  int a = 10;
  int b = 5;
  int c = a + b - (a * b) / (a % b);
  a++;
  b--;
  
  if (a < b) {
    // Menor que
  }
  if (a > b) {
    // Mayor que
  }
  
  switch (a) {
    case 1:
      break;
    default:
      break;
  }
}
/*Caracter(es) no reconocido lexicamente implementado para fallar a proposito */
@
class MyClass {}