// Prueba Sintáctica - Desarrollador 2 (Daniel Cortez)

double obtenerGravedad() => 9.81;
bool esMayorDeEdad() => true;

// ERROR SINTÁCTICO INTENCIONAL 1: Función flecha sin expresión ni valor de retorno
// El analizador arrojará error cerca del ';'
int funcionRota() => ;

void main() {
  int cantidadDeModulos = 5;
  double precioFinal = 19.99;
  bool? estadoNulable = null;
  String? nombreUsuario;

  Set<String> roles = {'Admin', 'User', 'Guest'};
  Set<double>? temperaturasNulables;
  Set conjuntoVacio = {};

  bool ejecutando = true;
  
  while (cantidadDeModulos >= 0 && ejecutando != false) {
    print(cantidadDeModulos);
    print("Ingrese un comando:");
  }

  // ERROR SINTÁCTICO INTENCIONAL 2: Bucle while sin paréntesis alrededor de la condición
  // El analizador arrojará error cerca de 'ejecutando'
  while ejecutando == true {
    print("Esto no deberia compilar");
  }

  String? entrada = stdin.readLineSync();
}