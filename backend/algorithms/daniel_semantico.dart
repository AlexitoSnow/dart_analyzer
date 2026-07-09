// Prueba Semántica - Desarrollador 2 (Daniel Cortez)

void main() {
  int x = 5;
  int x = 10; // Error Semantico: La variable 'x' ya esta declarada en este alcance.

  if (true) {
    int y = 20;
  }
  y++; // Error Semantico: La variable 'y' esta fuera de alcance (scope) o no ha sido declarada.
}
