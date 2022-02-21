document.addEventListener('DOMContentLoaded', () => {
  /*
   * LOGIN/REGISTER ANIMATION
   */
  const labels = document.querySelectorAll('.form-element label')

  labels.forEach((label) => {
    label.innerHTML = label.innerText
      .split('') // split into an array
      .map(
        (letter, idx) =>
          `<span style="transition-delay:${idx * 50}ms">${letter}</span>`
      ) // mapping it to create an array with a span around it
      .join('') // turn it back into a string
  })

  /*
   * MOBILE BURGER MENU
   */
  const burger = document.getElementById('burger')
  const sidebar = document.getElementById('sidebar')
  let counter = 0

  if (burger && sidebar) {
    burger.onclick = () => {
      if (counter % 2 === 0) {
        sidebar.style.width = `${window.innerWidth}px`
        sidebar.style.left = '0px'
      } else {
        sidebar.style.left = `-${window.innerWidth}px`
      }
      counter++
    }
  }

  /*
   * LOGOUT BTN
   */
  const cog = document.getElementById('cog')
  const logoutBtn = document.getElementById('logout')
  let ctn = 0

  if (cog && logoutBtn) {
    cog.onclick = () => {
      if (ctn % 2 === 0) {
        logoutBtn.style.display = 'inline-block'
        logoutBtn.style.opacity = '1'
      } else {
        logoutBtn.style.display = 'none'
        logoutBtn.style.opacity = '0'
      }
      ctn++
    }
  }
})
