angular.module('seao', ['ui.directives', 'ui.bootstrap', 'restangular', 'ngGrid'])
    .config(function(RestangularProvider) {
	RestangularProvider.setBaseUrl('/api/v1');
	RestangularProvider.setRequestSuffix('/?');
	RestangularProvider.setListTypeIsArray(false);
    });


function MainCtrl($scope, Restangular) {
    $scope.availColumns = [];
    $scope.selectedColumns = {};
    $scope.gridFields = [];
    $scope.gridOptions = {
	data: 'avis',
	columnDefs: 'gridFields'
    }

    var firstLoad = true;
    Restangular.all('avis').getList().get('objects').then(function(objs){
	$scope.avis = objs;
	console.log('test');
	if (objs.length) {
	    for (pr in objs[0]){
		$scope.availColumns.push(pr);
		if (firstLoad){
		    $scope.selectedColumns[pr] = false;
		    if (pr == 'numero') {
			$scope.selectedColumns[pr] = true;
		    }
		}
	    }
	    if (firstLoad){
		$scope.$broadcast('colChanged', $scope.selectedColumns);
		firstLoad = false;
	    }

	}
    });

    $scope.$on('colChanged', function(evt, selectedCols){
	console.log('received');
	var tmpFields = []
	for (var col in selectedCols) {
	    if (selectedCols[col]) {
		tmpFields.push({
		    field: col,
		    displayName: col
		})
	    }
	}
	$scope.gridFields = tmpFields;
    });
}
