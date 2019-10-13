window.addEventListener("DOMContentLoaded", function() {
    window.ver_dropdown = document.getElementById("ver-dropdown");
    window.sel_index = window.ver_dropdown.selectedIndex;
    window.ver_dropdown.style.display = "inline";
});

function dropdown_navigate(dest) {
    window.ver_dropdown.selectedIndex = window.sel_index;
    window.location = dest;
};
