let dark = document.querySelector('#dark-theme-btn')
let light = document.querySelector('#light-theme-btn')
let root = document.documentElement

dark.onclick = () => {
    root.style.setProperty('--background-color', '#333')
    root.style.setProperty('--text-color', '#fff')
}

light.onclick = () => {
    root.style.setProperty('--background-color', '#fff')
    root.style.setProperty('--text-color', '#333')
}
