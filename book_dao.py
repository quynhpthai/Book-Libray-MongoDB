from pymongo_connector import collection_B
from pymongo_connector import collection_P
def findAll():#queries all 
    results = collection_B.find({})
    return results


def findByTitle(book_title): # queries by title
    results = collection_B.find({'title': book_title})
    return results
def findbyPublisher(publisher):# queries using publisher
    results = collection_B.find({'published_by': publisher})
    return results
def findByPrice(min,max): #find using min and max
    results=collection_B.find({"$and": [{"price": {"$gte": min}}, {"price":{"$lte":max}}]}) 
    return results
def findByTitlePublisher(title,publisher):#find the book with the same title and publisher
    query = {
        "$and": [
            {'title': {'$regex': title, '$options': 'i'}},
            {'published_by': {'$regex': publisher, '$options': 'i'}}
        ]
    }
    results = collection_B.find(query)
    return results
def addPublisher(name, phone, city): # add publisher
    publisher_data={
        "name": name,
        "phone": phone,
        "city":city
    }
    try:
        collection_P.insert_one(publisher_data)
    except Exception as e:
        return f"Error: {str(e)}"
    return "Publisher " + name+ " added successfully"
def addBook( ISBN, title, year, published_by, previousEdition, price): # add book
    book_data={
        "ISBN": ISBN,
        "title": title,
        "year": year,
        "published_by": published_by if published_by != "NULL" else None,
        "previous_edition": previousEdition if previousEdition!="NULL" else None,
        "price":price
    }
    try:
        collection_B.insert_one(book_data)
    except Exception as e:
        return f"Error: {str(e)}"
    return "Book " + title+ " added successfully"
def editBook(ISBN,new_title,new_year,new_published_by,new_previous_edition,new_price): # edit book
    update_data = {
        "title": new_title,
        "year": new_year,
        "published_by": new_published_by,
        "previous_edition": new_previous_edition,
        "price": new_price
    }

    # Updating the book with the given ISBN
    try:
        result = collection_B.update_one({"ISBN": ISBN}, {"$set": update_data})
    except Exception as e:
        return f"Error: {str(e)}"

    if result.matched_count > 0:
        print(f"Book with ISBN {ISBN} updated successfully.")
    else:
        print(f"No book found with ISBN {ISBN}.")
def deleteBook(ISBN): # delete book
    try:
        result = collection_B.delete_one({"ISBN": ISBN})
    except Exception as e:
        return f"Error: {str(e)}"

    if result.deleted_count > 0:
        print(f"Book with ISBN {ISBN} was deleted successfully.")
    else:
        print(f"No book found with ISBN {ISBN}.")


