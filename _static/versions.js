window.addEventListener("DOMContentLoaded", function() {
    var opts = window.DOCUMENTATION_OPTIONS;

    // Load in version index
    $.getJSON(opts.URL_ROOT + "../_versions.json", function(versions) {
        window.versionDropdown = document.getElementById("ver-dropdown");
        if (!window.versionDropdown) {
            return;
        }
        window.versionIndex = 0;

        var pathComponents = window.location.pathname.split(/[\/\\]+/g);
        if (opts.URL_ROOT[0] === '/') {
            // Absolute path, eg. in case of the 404 page.
            window.versionRoot = opts.URL_ROOT.replace(/\/[^\/]+\/?$/g, '');
            var numComponents = (window.versionRoot.match(/\//g) || []).length;
            window.currentPagePath = pathComponents.slice(numComponents + 2).join('/');
        } else {
            var numComponents = (opts.URL_ROOT.match(/\.\./g) || []).length;
            window.versionRoot = pathComponents.slice(0, pathComponents.length - numComponents - 2).join('/');
            window.currentPagePath = pathComponents.slice(pathComponents.length - numComponents - 1).join('/');
        }

        // Create a select option for each version
        var isOutdated = false;
        var latestVersion = null;
        for (var i = 0; i < versions.length; ++i) {
            var version = versions[i];
            var opt = document.createElement('option');
            opt.value = version.version;
            opt.innerHTML = version.version;
            if (version.tag) {
                opt.innerHTML += ' (' + version.tag + ')';
            }
            if (version.version == opts.VERSION || opts.VERSION.indexOf(version.version + '.') === 0) {
                window.versionIndex = i;
                if (version.outdated) {
                    isOutdated = true;
                }
            } else if (version.hidden) {
                continue;
            }
            window.versionDropdown.appendChild(opt);
            if (version.latest) {
                latestVersion = version.version;
            }
        }

        // Hide the static version number, showing the dropdown instead
        document.getElementById("version-static").style.display = "none";
        document.getElementById("version-dynamic").style.display = "block";
        window.versionDropdown.selectedIndex = window.versionIndex;

        if (isOutdated) {
            const latestPath = window.versionRoot + '/' + latestVersion + '/' + window.currentPagePath;
            $('div.document').prepend('<div class="admonition warning"><p class="first admonition-title">Note</p><p class="last">You are browsing the documentation for an obsolete version. <a href="' + latestPath + '">Click here</a> to go to the latest version.</p></div>');
        }
    });
});

function switchVersion(version) {
    window.versionDropdown.selectedIndex = window.versionIndex;
    window.location.pathname = window.versionRoot + '/' + version + '/' + window.currentPagePath;
};
