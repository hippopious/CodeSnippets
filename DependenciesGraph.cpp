// Graph dependency manager. (A probably less optimized version of the Boost graph lib)

// Need to be able to install a component, uninstall a component, add component dependencies, and list all components
// Will create a class to manage the components.
// Will create a node structure to represent each component.

// For this implementation, we will not implement the "supports" data structure. This will make removals easier, but make installing a bit longer

#include <iostream>
using std;

struct Component
{
    string Name = null;
    ComponentDependency* ComponentDependencies = null;
    bool isInstalled = false;
    Component* NextComponent = null;
    
    ~Component()
    {
        // Complete this later :D Delete the component and component dependency data structs
    };
}

struct ComponentDependency
{
    Component* Dependency = null;
    ComponentDependency* NextDependency = null;
}

class DependenciesManager
{
    DependenciesManager()
    {
        // Initiate variables
    };
    
    ~DependenciesManager()
    {
        // Release all memory. Each component should rely on its own destructor
    };
    
    Component* ComponentList;
    int ComponentCount;         // This might not be necessary
    
    // Checks that the component to install isn't already installed, then
    // check whether dependencies are installed first, and finally,
    // it is installed. Example: Component A that depends on component B will always
    // be installed earlier in the list than component B, so we do not need to re-traverse the list of components
    bool InstallComponent(int componentName)
    {
        Component* currentComponent = ComponentList;
        
    };
    
    // Checks if the component already exists (regardless of installation state, and then
    // Checks if the new dependency will cause circular dependency. If ok, dependency is added. If not, return false
    bool AddDependency (string componentName; string dependencyName)
    {
        Component* currentComponent = ComponentList;
        bool componentNodeLocation = null;
        bool dependencyNodeLocation = null;
        
        // List is empty! Populate the graph with its first vertex and edge (dependency). No circular dependency is possible
        if (ComponentList == null)
        {
            // Create the first component
            ComponentList = new Component;
            ComponentList.Name = componentName;
            // Create another component representing the dependency and then link the component to its dependency
            ComponentList.NextComponent = new Component;
            ComponentList.NextComponent.Name = dependencyName;
            ComponentList.Dependencies = new Dependency;
            ComponentList.Dependencies.Dependency = ComponentList.NextComponent;
        }
        
        // Go through the components and mark where the component is and where the dependency is, if it exists
        // If dependency doesn't exist, we create it (good, easy). If it does, it either causes a circular dependency (bad) or it doesn't (good)
        while (currentComponent != null)
        {
            if componentName == currentComponent.Name
            {
                componentNodeLocation = currentComponent;
            }
            else if (dependencyName == currentComponent.Name)
            {
                dependencyNodeLocation = currentComponent;
            }
            
            currentComponent
        }
        
        // If this is a new component we're adding, then just tack it onto the end. There cannot be a circular dependency
            
        }
        
        // Traverse the thing and find a 
        do
        {
            
        }
    };
    
    // Checks that the component to be removed is not currently supporting anything that is installed.
    // Returns true if component is uninstalled
    // Returns false if component is still needed or if it doesn't exist.
    // In the future, we can be fancier and return an H-ERROR code.
    bool RemoveComponent(int componentName)
    {
        bool foundComponent = false;
        Component* currentComponent = ComponentList;
        while (currentComponent != null)
        {
            // Make sure the component we want to uninstall is present
            if (currentComponent == componentName)
            {
                foundComponent = true;
            }
            
            // Make sure all components depending on this component is not installed
            if ( (currentComponent != null) || (currentComponent.Name != componentName) )
            {
                currentDependency = currentComponent.Dependencies;
                while (currentDependency != null)
                {
                    if ( (currentDependency == componentName) && currentComponent.isInstalled == true)
                    {
                        return false;
                    }
                } 
            }
        }
        
        // Dependencies checked. Return whether we found the component or not
        return foundComponent;
    };

    // Lists all components by their name
    void ListComponents()
    {
        Component* currentComponent = ComponentList;
        while (currentComponent != null)
        {
            if (currentComponent.Name != null)
            {
                count << "Component name: " << currentComponent.Name << endl;
            }
            
            currentComponent = currentComponent.NextComponent;
        }
    };
    
}