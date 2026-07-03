const input = document.getElementById("fileInput");
const fileName = document.getElementById("fileName");
const progress = document.getElementById("progressBar");
const dropArea = document.getElementById("dropArea");

if (input) {

    input.addEventListener("change", function () {

        if (input.files.length > 0) {

            fileName.innerHTML = "✅ " + input.files[0].name;

            let width = 0;

            let timer = setInterval(function () {

                width += 5;

                progress.style.width = width + "%";

                if (width >= 100) {

                    clearInterval(timer);

                }

            }, 50);

        }

    });

}

// Counter Animation

const counters=document.querySelectorAll(".stat-card h2");

counters.forEach(counter=>{

const update=()=>{

const target=parseInt(counter.innerText);

let count=0;

const inc=target/60;

const timer=setInterval(()=>{

count+=inc;

if(count>=target){

counter.innerText=target+"+";

clearInterval(timer);

}else{

counter.innerText=Math.floor(count)+"+";

}

},25);

}

update();

});