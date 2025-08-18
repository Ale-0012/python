// let ph = 7;

// if (ph > 7){
//   console.log("Basico");
// }else if (ph < 7){
//   console.log(ph < 7)
//   console.log("Acido");
// }else{
//   console.log("Neutral")
// }

// Write code below 💖

// Write code below 💖

//56

// aire = 500;

// if (aire >= 0 && aire <= 50 ){
//   console.log('Bueno')
// }else if (aire >=51 && aire <= 100){
//   console.log('Moderado')
// }else if (aire >= 101 && aire<=150){
//   console.log('No saludable(grupos sensibles)')
// } else if (aire >=151 && aire<=200){
//   console.log('No saludable')
// }else if (aire >=201 && aire<= 300){
//   console.log('Muy insalubre')
// }else{
//   console.log('Peligroso')
// }

const uno = "piedra";
const dos = "papel";
const tres = "tijeras";

// Ingresa tu opción: uno, dos o tres
let user = uno; // Cambia a uno, dos o tres según quieras
let computer = Math.floor(Math.random() * 3) + 1;

let respComputer;
if (computer === 1) {
  respComputer = uno;
} else if (computer === 2) {
  respComputer = dos;
} else {
  respComputer = tres;
}

// Mostrar elecciones
console.log(`Computer: ${respComputer}     User: ${user}`);

// Determinar resultado
if (respComputer === user) {
  console.log("Empate");
} else if (
  (respComputer === uno && user === dos) ||  // piedra vs papel
  (respComputer === dos && user === tres) || // papel vs tijeras
  (respComputer === tres && user === uno)    // tijeras vs piedra
) {
  console.log("Ganas");
} else {
  console.log("Pierdes");
}