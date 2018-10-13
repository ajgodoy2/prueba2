Vue.component("home", {
    template: "<h1>Home {{picks}}</h1>",
    data: function () {
        return {picks: [1, 2]}
    }
});

var mode = "main";

new Vue({
    el: "#app"
});

function refresh() {
    if (mode === "main") {
        $("#app").html("<home></home>");
    }
}

//refresh();