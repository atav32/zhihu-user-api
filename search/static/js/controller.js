function searchController($scope, $http) {

    console.log($scope);

    function onSuccess(data, status, headers, config) {
        $scope.user = data;
        console.log($scope);
    }

    function onError(data, status, headers, config) {
        console.log("Error");
    }

    $scope.search = function() {
        $http({
            method: 'GET', 
            url: location.pathname + 'api/?name=' + $scope.username
        })
        .success(onSuccess)
        .error(onError);
        return $scope.user;
    }
}
