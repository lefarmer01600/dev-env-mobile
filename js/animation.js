window.addEventListener(
    "scroll",
    () => {
        document.body.style.setProperty(
            "--scroll",
            (window.scrollY / (document.body.offsetHeight - window.innerHeight))*-30
        );
    },
    false
);