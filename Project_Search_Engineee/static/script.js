        function createLeaf(){
            const leaf = document.createElement("div");
            leaf.classList.add("leaf");
            leaf.innerHTML = "🍁";

            leaf.style.left = Math.random() * window.innerWidth + "px";
            leaf.style.animationDuration = (Math.random() * 3 + 3) + "s";

            document.body.appendChild(leaf);

            setTimeout(()=>{
                leaf.remove();
            },6000);
        }

        setInterval(createLeaf, 500);
