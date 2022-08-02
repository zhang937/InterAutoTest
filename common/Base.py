import re

from config.Conf import ConfigYaml
from utils.MysqlUtil import MysqlUtil
from utils.AssertUtil import AssertUtil


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


def init_db(db_alias):
    """

    :param db_alias:
    :return:
    """
    db_info=ConfigYaml().get_db_conf_info( db_alias )
    host=db_info['host']
    user=db_info["user"]
    password=db_info["password"]
    database=db_info['database']
    charset=db_info['charset']
    port=db_info['port']
    conn=MysqlUtil( host, user, password, database, charset, port )
    return conn


def assert_db(db_name, result, db_verify):
    """

    :param db_name:
    :param result:
    :param db_verify:
    :return:
    """
    sql=init_db( db_name )
    db_res=sql.fetchone( db_verify )
    verify_list=list( dict( db_res ).keys() )
    for line in verify_list:
        res_line=result[line]
        res_db_line=dict( db_res )[line]
        AssertUtil().assert_body( res_line, res_db_line )


def res_find(data, pattern_data='\${(.*)}\$'):
    """

    :param data:
    :param pattern_data:
    :return:
    """
    # pattern=re.compile( '\${(.*)}\$' )
    pattern=re.compile( pattern_data )
    return pattern.findall( data )


def res_sub(data, replace, pattern_data='\${(.*)}\$'):
    """

    :param data:
    :param replace:
    :param pattern_data:
    :return:
    """
    pattern=re.compile( pattern_data )
    re_res=pattern.findall( data )
    if re_res:
        return re.sub( pattern_data, replace, data )
    return re_res


def params_find(headers, cookies):
    """
    验证请求中是否存在需要的参数。
    :param headers:
    :param cookies:
    :return:
    """
    if "${" in headers:
        headers=res_find( headers )
    if "${" in cookies:
        cookies=res_find( cookies )
    return headers, cookies


if __name__ == '__main__':
    print( res_sub( '{"Authorization":"JWT ${token}$"}', '333333' ) )
