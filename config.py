"""config.py"""
import os


class Config:
    """
    Config
    """

    def __init__(self) -> None:
        """
        Constructor<br>
        -----------<br>

        Variables denoting a path - including or excluding a filename - have an underscore suffix; this suffix is
        excluded for names such as warehouse, storage, depository, etc.<br><br>
        """

        '''
        Keys
        '''
        self.s3_parameters_key = 's3_parameters.yaml'
        self.argument_key = 'assets/arguments.json'


        '''
        Cloud Prefix: Metadata [vis-à-vis Configurations Bucket]
        '''
        self.metadata_ = 'assets/external'


        '''
        Project Metadata
        '''
        self.project_tag = 'hydrography'
        self.project_key_name = 'HydrographyProject'


        '''
        Local Paths
        '''
        self.warehouse = os.path.join(os.getcwd(), 'warehouse')
        self.pathway_ = os.path.join(self.warehouse, 'assets')
        self.maps_ = os.path.join(self.pathway_, 'maps')


        '''
        Cloud Prefix: Destination
        '''
        self.prefix = self.pathway_.replace(os.getcwd() + os.sep, '')
