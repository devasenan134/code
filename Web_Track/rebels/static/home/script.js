function file_reader(file) {
    const reader = new FileReader()
    reader.onload = () => {
        console.log(reader.result)
    }
    reader.readAsText(file)
}


const real_file_btn = document.querySelector('#real-file-btn')
const custom_file_btn = document.querySelector('#custom-file-btn')
const file_format_msg = document.querySelector('#file-format-msg')
const file_name = document.querySelector('#file-name')

const file_content = document.querySelector("#file-content")

custom_file_btn.addEventListener('click', () => {
    real_file_btn.click()
})

real_file_btn.addEventListener('change', () => {
    const file_data = real_file_btn.files[0]
    const extention = file_data.type.split('/')
    console.log(file_data)
    if (extention[1] === 'pdf') {
        file_name.innerHTML = `${file_data.name}`
        file_reader(file_data)
        file_content.innerHTML = file_data
    } else {
        console.log("Not a pdf")
        file_format_msg.innerHTML = 'File choosen is not PDF'
    }
    
}, false)


