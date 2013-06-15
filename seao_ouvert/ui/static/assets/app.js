angular.module('seao', ['ui.directives', 'ui.bootstrap', 'restangular', 'ngGrid'])
    .config(function(RestangularProvider) {
	RestangularProvider.setBaseUrl('/api/v1');
	RestangularProvider.setRequestSuffix('/?');
	RestangularProvider.setListTypeIsArray(false);
    });
function MainCtrl($scope, Restangular) {
    $scope.avis = Restangular.all('avis').getList().get('objects');

    $scope.gridOptions = {
	data: 'avis'
    };
}
