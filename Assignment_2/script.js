function calculate(){
    var inp = document.cal.numbers.value;
    var x = inp.split(",").map(function(item)
    {
        return parseFloat(item.trim());
    });
    if (x.length!=0){
        var max = maxi(x);
        var min = mini(x);
        var su = sum(x);
        var av = avg(x);
        var re = rev(x);
    }
    document.getElementById("max").textContent = "Max: " + max;
    document.getElementById("min").textContent = "Min: " + min;
    document.getElementById("sum").textContent = "Sum: " + su;
    document.getElementById("avg").textContent = "Avarage: " + av;
    document.getElementById("rev").textContent = "Reverse Order: " + re ;
}

function maxi(a){
    return Math.max(...a);
}
function mini(a){
    return Math.min(...a);
}
function sum(a){
    return a.reduce((acc, num) => acc + num, 0);
}
function avg(a){
    let s = sum(a);
    return s/a.length
}
function rev(a){
    return a.slice().reverse();
}

function convert(){
    const w = parseFloat(document.getElementById("val").value);
    const choice = document.getElementById("choice").value;

    if (choice === "ktl"){
        var res = w*0.4536;
        document.getElementById("result").textContent = `${res.toFixed(4)} pounds`;
    } 
    else if (choice === "ltk"){
        var res = w*2.2046;
        document.getElementById("result").textContent =`${res.toFixed(4)} kilograms`;
    }
}

function qt(){
    const q = [
        "The less we deserve good fortune, the more we hope for it.",
        "Fortune and love favor the brave.",
        "Formal education will make you a living; self-education will make you a fortune.",
        "Live as brave men; and if fortune is adverse, front its blows with brave hearts.",
        "Fortune favors the prepared mind.",
        "Fortune befriends the bold.",
        "Come what may, all bad fortune is to be conquered by endurance.",
        "There are good and bad times, but our mood changes more often than our fortune.",
        "Fortune favors the audacious.",
        "From my tribe I take nothing, I am the maker of my own fortune.",
        "Diligence is the mother of good fortune.",
        "Friends and acquaintances are the surest passport to fortune."
        ]

    document.getElementById("qu").textContent = q[Math.floor(Math.random() * q.length)];
    
}
window.onload = qt;


function colors(x){
    const colors = {
        p: { bg: "#FF9BD2", border: "#D63484", text: "#402B3A", f: "15px", ff:"Trebuchet MS"}, 
        b: { bg: "#068FFF", border: "#4E4FEB", text: "#000000", f:"17px", ff:"Arial"}, 
        o: { bg: "#F05941", border: "#872341", text: "#22092C", f: "20px", ff:"Lucida Grande"}, 
        pu: { bg: "#C147E9", border: "#810CA8", text: "#2D033B", f: "22px", ff:"sans-serif"} 
    };
    const clr = colors[x];
    const box2 = document.querySelector(".box2");
    const text = document.querySelector("#qu");

    box2.style.backgroundColor = clr.bg;
    box2.style.borderColor = clr.border;
    box2.style.fontSize = clr.f;
    box2.style.fontSize = clr.ff;
    text.style.color = clr.text;

}