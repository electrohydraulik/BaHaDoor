# Baha-Centralized

## Description

This is an membership rights service for use in entities such as Fab-labs, Makerspaces, Hackerspaces. This should be a frame work for expansion for user rights to coarse access to buildings down to asset rental.

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the expected value of the `data field`

### List all members

**Definition**

`GET /members`

**Response**

- `200 OK` on success

```json
[
    {
        "UID": "1510725",
        "name": "John Doe",
        "class": "member",
        "Access": "True"
    },
    {
        "UID": "669686",
        "name": "Ro Boh",
        "class": "officer",
        "Access": "True"
    }
]
```

### Registering a new Member

**Definition**

`POST /members`

**Arguments**

- `"UID":string` the id number of the member access tag
- `"name":string` Member Name
- `"class":string` Status of member in the organization
- `"Access":string` Has access to building

If a device with the given identifier already exists, the existing device will be overwritten.

**Response**

- `201 Created` on success

```json
{
    "UID": "1510725",
    "name": "John Doe",
    "class": "member",
    "Access": "True"
}
```

## Lookup member details

`GET /member/<identifier>`

**Response**

- `404 Not Found` if the member does not exist
- `200 OK` on success

```json
{
    "UID": "1510725",
    "name": "John Doe",
    "class": "member",
    "Access": "True"
}
```

## Delete a Member

**This should only be used if a member returns their RFID tag or a new tag is issued**

**Definition**

`DELETE /devices/<identifier>`

**Response**

- `404 Not Found` if the member does not exist
- `204 No Content` on success