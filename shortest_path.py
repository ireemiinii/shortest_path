origin_layer =  QgsProject.instance().mapLayersByName('origin_points')[0]
destination_layer =  QgsProject.instance().mapLayersByName('destination_points')[0]
matrix =  QgsProject.instance().mapLayersByName('nearest_destination')[0]

for f in matrix.getFeatures():
    origin_expr = QgsExpression('cnn={}'.format(f['origin_id']))
    destination_expr = QgsExpression('cnn={}'.format(f['destination_id']))
    origin_feature = origin_layer.getFeatures(QgsFeatureRequest(origin_expr))
    origin_coords =  [(f.geometry().asPoint().x(), f.geometry().asPoint().y())
        for f in origin_feature]
    destination_feature = destination_layer.getFeatures(QgsFeatureRequest(destination_expr))
    destination_coords =  [(f.geometry().asPoint().x(), f.geometry().asPoint().y())
        for f in destination_feature]
    params = {
        'INPUT':'geo_export_df7a8003-4b3f-4bd4-aa9c-0bae12b615f9',
        'START_POINT':'{},{}'.format(origin_coords[0][0], origin_coords[0][1]),
        'END_POINT':'{},{}'.format(destination_coords[0][0], destination_coords[0][1]),
        'STRATEGY':0,
        'ENTRY_COST_CALCULATION_METHOD':0,
        'DIRECTION_FIELD':'oneway',
        'VALUE_FORWARD':'B\n',
        'VALUE_BACKWARD':'T\n',
        'VALUE_BOTH':'',
        'DEFAULT_DIRECTION':2,
        'SPEED_FIELD':None,
        'DEFAULT_SPEED':5,
        'TOLERANCE':0,
        'OUTPUT':'memory:'}
    print('Executing analysis')
    processing.runAndLoadResults("qneat3:shortestpathpointtopoint", params)