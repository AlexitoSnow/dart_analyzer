// Prueba Sintáctica - Desarrollador 3 (Alexander Nieves)

class Vehiculo {
  void arrancar() {}
}

class Auto extends Vehiculo {
  void detener() {}
}

// ERROR SINTÁCTICO INTENCIONAL 1: Se usa 'extends' pero no se indica la clase padre
// El analizador arrojará error cerca de '{'
class Moto extends {
  void acelerar() {}
}

void procesarDatos() {
}

void main() {
  final int limiteMaximo = 100;
  const double valorPi = 3.14159;
  final configuracion = true;

  List<int> numeros = [10, 20, 30];
  List<String> nombres = ['Alex', 'Sofia'];
  List listaVacia = [];

  int resultado = (10 + 5) * 2 / 3 - 1 % 2;

  for (int i = 0; i <= 5; i++) {
    resultado++;
    resultado--;
  }

  // ERROR SINTÁCTICO INTENCIONAL 2: Bucle For incompleto, falta el incremento (ej. i++)
  // El analizador arrojará error cerca de ')'
  for (int i = 0; i < 10;) {
    resultado++;
  }

  switch (resultado) {
    case 10:
      break;
    case 20:
      break;
    default:
      break;
  }
}