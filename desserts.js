let cartvalue=0

const cartcount=document.getElementById("cart-value")

function increase(){
    cartvalue++
    cartcount.textContent=cartvalue
}
const buycount=document.querySelectorAll(".buy-button")
buycount.forEach(button => {
    button.addEventListener('click',increase)
});