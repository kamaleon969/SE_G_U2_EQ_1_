//String dato = "E001R056R300C";     
String dato="";             //String que recibe desde python
int numeros[3];
char* dividir = NULL;           //apuntador de caracteres
int i = 0,led1=2,led2=3,led3=4;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {                     
    dato = Serial.readString();                     
    if (dato.charAt(0) == 'E' && dato.charAt(dato.length() - 1) == 'C') {       
      dato = dato.substring(1, dato.length() - 1);                
      char* cad = dato.c_str();                     
      dividir = strtok(cad, "R");                     
      int cont = 0;                         
      while (dividir != NULL) {                     
        numeros[cont] = String(dividir).toInt();                
        dividir = strtok(NULL, "R");                    
        cont++;                           
      }
      Serial.println("");
      Serial.println("--------");
      for (i = 0; i < 3; i++) {                     
        Serial.println(numeros[i]);                      
      }

      analogWrite(led1,numeros[0]);
      analogWrite(led2,numeros[1]);
      analogWrite(led3,numeros[2]);
    }
    else{
      Serial.println("La cadena no es valida!!");
      Serial.println("Estructura: E(num1)R(num2)R(num3)C");
    }
  }
}
