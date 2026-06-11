from abc import ABC, abstractmethod

class PageInterface(ABC):
    """
    PageInterface — defines the CONTRACT.
    Every page class MUST implement these methods.
    Cannot be instantiated directly.
    """
    
    @abstractmethod
    def open(self, url):
        """Every page must implement how it opens"""
        pass

    @abstractmethod
    def is_loaded(self):
        """Every page must implement how to verify it loaded"""
        pass

    @abstractmethod
    def get_page_title(self):
        """Every page must implement how to get its title"""