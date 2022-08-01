def get_item_by_key(obj, key, result=None):
    """
    获取接口请求响应中指定key及其内容
    :param obj:
    :param key:
    :param result:
    :return:
    """
    if isinstance( obj, dict ):
        for k in obj:
            if key == k:
                if isinstance( result, list ):
                    if isinstance( obj[k], list ):
                        result.extend( obj[k] )
                    else:
                        result.append( obj[k] )
                elif result is None:
                    result=obj[k]
                else:
                    tmp=[result]
                    result=tmp
                    result.append( obj[k] )
            else:
                if isinstance( obj[k], dict ) or isinstance( obj[k], list ):
                    result=get_item_by_key( obj[k], key, result )
    elif isinstance( obj, list ):
        for i in obj:
            if isinstance( i, dict ) or isinstance( i, list ):
                result=get_item_by_key( i, key, result )
    return result[0] if isinstance( result, list ) and len( result ) == 1 else result
