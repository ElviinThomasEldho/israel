const allSections = document.querySelectorAll(".section");

// const revealSection = function (entries, observor) {
//   const [entry] = entries;
//   if (!entry.isIntersecting) return;
//   entry.target.classList.remove("section--hidden");
//   sectionObservor.unobserve(entry.target);
// };

// const sectionObservor = new IntersectionObserver(revealSection, {
//   root: null,
//   threshold: 0.1,
// });

// allSections.forEach(function (section) {
//   sectionObservor.observe(section);
//   section.classList.add("section--hidden");
// });

(function () {
  // https://dashboard.emailjs.com/admin/account
  emailjs.init("gP6L_j8HqKiURVM4z");
})();

window.onload = function () {
  document
    .getElementById("contact-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      // generate a five digit number for the contact_number variable
      this.contact_number.value = (Math.random() * 100000) | 0;
      // these IDs from the previous steps
      console.log(this);
      emailjs.sendForm("service_tpkxkl6", "template_9oi5huv", this).then(
        function () {
          console.log("SUCCESS!");
        },
        function (error) {
          console.log("FAILED...", error);
        }
      );
    });
};

const btnTranslate = document.getElementById("translate");
const sectionEN = document.getElementsByClassName("english")[0];
const sectionHB = document.getElementsByClassName("hebrew")[0];
console.log(btnTranslate, sectionEN, sectionHB);

btnTranslate.addEventListener("click", () => {
  if (btnTranslate.textContent == "Translate to עִברִית") {
    btnTranslate.textContent = "Translate to English";
  } else {
    btnTranslate.textContent = "Translate to עִברִית";
  }

  sectionEN.classList.toggle("hidden");
  sectionHB.classList.toggle("hidden");
});
