__all__=["ConfURI","OSG"]
class ConfURI:
    BatchAddImageToDB={'method': 'POST', 'uri': '/engine/api-wrapper/v1/face/batch_add_image_to_db'}

class OSG:
    UpdateBucket = {'method': 'PUT', 'uri': '/components/osg-default/v1/{bucket_name}'}
