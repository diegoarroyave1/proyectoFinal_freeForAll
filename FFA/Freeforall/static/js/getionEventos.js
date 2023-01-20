const btnsEliminacion = document.querySelectorAll('.btnEliminacion');
const likeBtn = document.querySelector(".like_btn")
const count = document.querySelector("#count")
let clicked = false;

(function () {

    likeBtn.addEventListener("click", () =>{
        if (!clicked){
            clicked = true;
            count.textContent++;
            
        }else{
            clicked = false;
            count.textContent--;
            
        }
    });

    btnsEliminacion.forEach(btn => {
        btn.addEventListener('click' ,function(e) {
            let confirmacion = confirm("¿Esta seguro que quiere eliminar?");
            if(!confirmacion){
                e.preventDefault();
            }
        })
    });

})();