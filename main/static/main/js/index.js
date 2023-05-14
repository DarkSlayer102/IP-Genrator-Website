


ipv4 = document.querySelectorAll("li");

remove_button = document.querySelector("input")



let clicked = false
remove_button.addEventListener("click", (event)=>{
    for (let i=0;i< ipv4.length;i++) {
        clicked = true;
        ipv4[i].remove();
        window.location.href = "/remove"
        
    }
    

})



/*


function click_remove(){
    
    for (let i=0;i<ipv4.length;i++){
        ipv4[i].addEventListener("click",(event)=>{
            ipv4[i].parentNode.removeChild(ipv4[i])
        })
    }
}


click_remove();


*/
