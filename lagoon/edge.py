# -*- coding: utf-8 -*-
from .tools import to_string_url
from .entity import Entity


class Edge(Entity):
    """
    This class describes an Edge object child of Lagoon class.
    """
    def to_dict(self):
        """
        Convert the edge to a dictionary

        :returns:   The edge as a dictionary
        :rtype:     dictionary
        """

        return super(Edge, self).to_dict()

    def set_data_variables(self, data={}):
        """
        Sets the data variables of the object

        :param      data:  The object edge from Lagoon API
        :type       data:  dictionary
        """
        super(Edge, self).set_data_variables(data=data)
        self._from = data.get('_from', '')
        self._to = data.get('_to', '')

    def create(self, type='', from_key='', to_key='', data={}):
        """
        Create an edge

        .. tip::
            The type of the edge is case sensitive ! By convention, all edges' type start with a capital letter

        :param      type:      The edge type
        :type       type:      string
        :param      from_key:  The source key
        :type       from_key:  string
        :param      to_key:    The destination key
        :type       to_key:    string
        :param      data:      The edge data
        :type       data:      dictionary, optional

        :returns:   Edge object
        :rtype:     :class:`~lagoon.edge.Edge`
        """
        payload = dict(fromKey=from_key,
                       toKey=to_key,
                       type=type,
                       data=data)

        result = self.do_request('POST', 'edges', json=payload)
        result = self.parent.cast(result)
        return result

    def replace_data(self, data={}):
        """
        Replace the edge data with new ones

        .. danger::
            This is replacing all existing edge data. Meaning that you can loose data.


        :param      data:  The new edge data
        :type       data:  dictionary

        :returns:   Edge object
        :rtype:     :class:`~lagoon.edge.Edge`
        """
        data = dict(data=data)
        result = self.do_request(
            'PUT', 'edges/'+self._key, json=data)
        result = self.parent.cast(result)
        return result

    def update_data(self, data={}, deep_merge=True):
        """
        Update the edge data by merging the existing ones with the new ones

        :param      data:        The new edge data
        :type       data:        dictionary
        :param      deep_merge:  Merge nested objects
        :type       deep_merge:  boolean, optional

        :returns:   Edge object
        :rtype:     :class:`~lagoon.edge.Edge`
        """
        data = dict(
            data=data,
            deepMerge=deep_merge
        )
        result = self.do_request(
            'PATCH', 'edges/'+self._key, json=data)
        result = self.parent.cast(result)
        return result

    def get(self, populate=False):
        """
        Get the edge by its _key

        :param      populate:  Populate `edge.createdBy` and `edge.updatedBy` with User object
        :type       populate:  boolean, optional

        :returns:   Edge object
        :rtype:     :class:`~lagoon.edge.Edge`
        """
        result = self.do_request(
            'GET', 'edges/{0}/?populate={1}'.format(self._key, to_string_url(populate)))
        result = self.parent.cast(result)
        return result

    def delete(self):
        """
        Delete the edge

        .. danger::
            The edge will be completely deleted

        :returns:   Deleted edge object from API
        :rtype:     dictionary
        """
        result = self.do_request('DELETE', 'edges/' + self._key)
        return result
