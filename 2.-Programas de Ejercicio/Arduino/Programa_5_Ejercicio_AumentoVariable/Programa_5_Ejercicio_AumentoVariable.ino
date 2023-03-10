int Variable;

void setup() {
  Serial.begin(9600);
}

void loop() {
  Serial.println(Variable);
  Variable++;
  delay(500);
}
