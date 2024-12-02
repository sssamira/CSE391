function clearall(){
    document.querySelector('.txt_box').value = '';
}
flag = true;
function capi(){
    const txtbox = document.querySelector('.txt_box');
    const text = txtbox.value;
    if (!flag) {
        txtbox.value = text.toLowerCase();
    } else {
        txtbox.value = text.toUpperCase();
    }
    flag = !flag;
}
function sortt(){
    const txtbox = document.querySelector('.txt_box');
    const text = txtbox.value;
    txtbox.value = text.split('\n').sort((a, b) => a.trim().localeCompare(b.trim())).join('\n');
}
function rev(){
    const txtBox = document.querySelector('.txt_box');
    const text = txtBox.value;
    txtBox.value = text.split('\n').map(line => line.split('')
        .reverse()
        .join(''))
        .join('\n');
}
function stripblank(){
    const txtBox = document.querySelector('.txt_box');
    const text = txtBox.value;
    txtBox.value = text
        .split('\n')
        .map(line => line.trim())
        .filter(line => line !== '')
        .join('\n');
}
function addnum(){
    const txtBox = document.querySelector('.txt_box');
    const text = txtBox.value;
    txtBox.value = text
        .split('\n')
        .map((line, index) => `${index + 1}. ${line.trim()}`)
        .join('\n');
}
function shuff(){
    const txtBox = document.querySelector('.txt_box');
    const text = txtBox.value;
    const lines = text.split('\n');
    for (let i = lines.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [lines[i], lines[j]] = [lines[j], lines[i]]; 
    }
    txtBox.value = lines.join('\n');
}
