# Classes
A class in Active Directory serves as the blueprint for instantiating objects. Interestingly enough, each class definition is represented by an *object* in the Schema. More specifically, every class is an instance of the [classSchema](https://learn.microsoft.com/en-us/windows/win32/adschema/c-classschema?redirectedfrom=MSDN) built-in class.

```admonish note
Classes are very similar to data types in programming languages.
```

The object representing a class within the Schema (i.e. an object of type `classSchema`) has many attributes, but following are the most important ones:

|Attribute|Syntax|Description|
|:--|:--:|--:|
|`cn`|Unicode String|The common name from which the class's relative distinguished name (RDN) within the Schema is formed. It must be unique in the Schema.|
|`lDAPDisplayName`|Unicode String|The name used by LDAP clients to refer to the class. It must be unique in the Schema.|
|`adminDescription`|Unicode String|A description of the class for administrative applications.|
|`mustContain`, `systemMustContain`|Unicode String|This pair of multi-valued attributes specify the attributes that all instances of the class *must* contain.|
|`mayContain`, `systemMayContain`|Unicode String|This pair of multi-valued attributes specify *optional* attributes that instances of the class may or may not have.|
|`possSuperiors`, `systemPossSuperiors`|Unicode String|This pair of multi-valued attributes specify the classes that are allowed to be parents of the class.|
|`objectClassCategory`|Integer|The class's category (1 - Structural, 2 - Abstract, 3 - Auxiliary.|
|`subclassOf`||The OID of the immediate parent of the class. <br/>Structural classes may only have other structural or abstract classes as their parent. <br/>Abstract classes may only have other abstract classes as a parent. <br/>For auxiliary classes, `subclassOf` may be either an auxiliary or an abstract class.|
|`auxiliaryClass`, `systemAuxiliaryClass`||This pair of multi-valued properties specify the auxiliary classes that the class inherits from.|

## Class Categories
There are three class categories in Active Directory.

*Structural* classes are the most basic type of AD class and are the only classes which can be instantiated directly, i.e. one can create objects from them. These classes are allowed to inherit from abstract classes as well as other structural classes and are denoted in the corresponding `classSchema` object by an `objectClassCategory` of 1.

*Abstract* classes are classes which cannot be instantiated, i.e. it is not possible to create objects from them. They are commonly used as a stepping stone towards the construction of more sophisticated classes which need to share certain functionality. This is why abstract classes may only inherit from other abstract classes.

An abstract class is denoted in the corresponding `classSchema` object by an `objectClassCategory` of 2.

```admonish note
Abstract classes in Active Directory are very similar to abstract classes in programming languages.
```

*Auxiliary* classes serve mainly as a grouping mechanism and cannot be instantiated. They should be thought of simply as collections of attributes which structural and abstract classes can inherit. Auxiliary classes are denoted in the corresponding `classSchema` object by an `objectClassCategory` of 3 and may themselves only inherit from other auxiliary or abstract classes.

```admonish note
Auxiliary classes resemble, to a certain degree, interfaces in programming languages.
```

## Inheritance
The special thing about classes is that they can inherit from one another. This is done by specifying the parent of the class in its `subclassOf` attribute. Inheritance works by implicitly including the values of the `mustContain`, `systemMustContain`, `mayContain`, `systemMayContain` attributes of the parent class in those of the child. In this way, the child will have all of the mandatory and optional attributes of the parent. Similarly, the `possSuperiors` and `systemPossSuperiors` of the parent are also included in those of the child class. This process propagates backwards until the top of the ancestry tree - a child class inherits the properties of its parent class and all of its grandparent classes. 

Whilst Active Directory classes may only have a single immediate parent to inherit from, they are allowed to inherit attributes from multiple auxiliary classes by listing them in the `auxiliaryClass` and `systemAuxiliaryClass` attributes.

![](Resources/Images/Inheritance%20Tree%20of%20user.svg)

~~~admonish info title="The top Class"
The ancestry of any class in Active Directory can be traced back to the special class `top` (with the exception of `top` itself).
~~~
