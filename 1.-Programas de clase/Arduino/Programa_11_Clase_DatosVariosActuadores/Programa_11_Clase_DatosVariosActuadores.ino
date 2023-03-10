
void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);
  Serial.setTimeout(100);//ms por defecto 1000
}

String cadena;

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.available()>0){
    cadena = Serial.readString();
    Serial.println(cadena); 

    
       
  }

 
  delay(10);
  
}
