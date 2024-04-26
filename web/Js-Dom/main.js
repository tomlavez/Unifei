const btnGerarQ = document.getElementById("btnGerarQ");
const btnValidarRes = document.getElementById("btnValidarRes")

let resposta;

btnGerarQ.addEventListener('click', () => {
    const op1 = Math.floor(Math.random() * 10);
    const op2 = Math.floor(Math.random() * 10);

    const random = Math.floor(Math.random() * 3);
    const listaSinal = ["+", "*", "-"];
   
    sinal = listaSinal[random];

    resposta = exec(op1, op2, sinal);

    document.getElementById("idAreaEquacao").innerHTML = `${op1} ${listaSinal[random]} ${op2}`;

})

function exec (op1, op2, sinal) {
    switch (sinal) {
        case "+":
            return op1 + op2;
        case "*":
            return op1 * op2;
        case "-":
            return op1 - op2;
        default:
            return "Error"
    }
}

btnValidarRes.addEventListener('click', () => {
    const ans = resposta;
    const pCor = document.querySelector('#idAreaResp');

    const userAns = document.querySelector("#resposta").value;

    if (ans === undefined){
        document.querySelector("#idAreaResp").innerText = "Gere uma equação primeiro!"
        pCor.classList.remove('corAzul')
        pCor.classList.add('corVermelha')
    }
    else if (Number(userAns) === ans){
        document.querySelector("#idAreaResp").innerText = "Parabéns!"
        pCor.classList.remove('corVermelha')
        pCor.classList.add('corAzul')
    }
    else {
        document.querySelector("#idAreaResp").innerText = `Deu Ruim! A resposta correta é ${ans}`
        pCor.classList.remove('corAzul')
        pCor.classList.add('corVermelha')
    }
})
