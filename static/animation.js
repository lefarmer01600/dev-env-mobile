window.addEventListener(
    "scroll",
    () => {
        document.body.style.setProperty(
            "--scroll",
            (window.scrollY / (document.body.offsetHeight - window.innerHeight)) * -30
        );
        if ((window.scrollY / (document.body.offsetHeight - window.innerHeight)) * -30 < -0.1) {
            document.getElementById("nav-btn-contact").innerHTML = "<a>Nous contacter</a>"
            document.getElementById("nav-btn-contact").classList.add("join-item")
            document.getElementById("nav-btn-contact").classList.add("btn")
            document.getElementById("nav-group").classList.remove("rounded-r-full")
            // "<li id='nav-btn-contact' class='btn join-item'><a>Nous contacter</a></li>"
        } else {
            document.getElementById("nav-btn-contact").innerHTML = ""
            document.getElementById("nav-btn-contact").classList.remove("join-item")
            document.getElementById("nav-btn-contact").classList.remove("btn")
            document.getElementById("nav-group").classList.add("rounded-r-full")
        }

        if ((window.scrollY / (document.body.offsetHeight - window.innerHeight)) * -30 < -27) {
            document.getElementById("nav-group").classList.add("bg-slate-400")
            document.getElementById("nav-group").classList.remove("glass")
        } else {
            document.getElementById("nav-group").classList.remove("bg-slate-400")
            document.getElementById("nav-group").classList.add("glass")
        }
    },
    false
);