document.body.addEventListener("mousemove", evt => {
  const mouseX = evt.clientX;
  const mouseY = evt.clientY;

  gsap.set(".cursor", {
    x: mouseX,
    y: mouseY });


  gsap.to(".shape", {
    x: mouseX,
    y: mouseY,
    stagger: -0.1 });

})

document.documentElement.style.setProperty('--shape-1', "#"+((1<<24)*Math.random()|0).toString(16));
document.documentElement.style.setProperty('--shape-2', "#"+((1<<24)*Math.random()|0).toString(16));
document.documentElement.style.setProperty('--shape-3', "#"+((1<<24)*Math.random()|0).toString(16));