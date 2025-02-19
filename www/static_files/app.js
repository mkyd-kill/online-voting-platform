// making a ul.li navlink active
document.addEventListener("DOMContentLoaded", () => {
    const sidebarLinks = document.querySelectorAll(".sidebarLink");
    const currentPath = window.location.pathname;

    sidebarLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath && currentPath.length > 2) {
            link.querySelector(".sidebarListItem").classList.add("active");
        }
    });
});