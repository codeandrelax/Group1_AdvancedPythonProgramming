#include <Python.h>
#include <string.h>

#define MAX_PASSWORD_LENGTH 1000

static PyObject* hash_password(PyObject* self, PyObject* args) {
    const char *pass;
    if (!PyArg_ParseTuple(args, "s", &pass)) {
        return NULL;
    }

    char key[] = "thisisthekey";
    char hashed_pass[MAX_PASSWORD_LENGTH + 1] = {0};

    int pass_length = strlen(pass);
    int key_length = strlen(key);

    if (pass_length > MAX_PASSWORD_LENGTH) {
        PyErr_SetString(PyExc_ValueError, "Password length exceeds maximum limit");
        return NULL;
    }

    for (int i = 0; i < pass_length; ++i) {
        hashed_pass[i] = pass[i] ^ key[i % key_length];
    }
    hashed_pass[pass_length] = '\0';

    return Py_BuildValue("s", hashed_pass);
}

static PyObject* check_password(PyObject* self, PyObject* args) {
    const char *hash, *pass;
    if (!PyArg_ParseTuple(args, "ss", &hash, &pass)) {
        return NULL;
    }

    char hashed_pass[MAX_PASSWORD_LENGTH + 1] = {0};

    int pass_length = strlen(pass);
    int key_length = strlen("thisisthekey");

    if (pass_length > MAX_PASSWORD_LENGTH) {
        PyErr_SetString(PyExc_ValueError, "Password length exceeds maximum limit");
        return NULL;
    }

    for (int i = 0; i < pass_length; ++i) {
        hashed_pass[i] = pass[i] ^ "thisisthekey"[i % key_length];
    }
    hashed_pass[pass_length] = '\0';

    int match = strcmp(hash, hashed_pass);
    if (match == 0) {
        Py_RETURN_TRUE;
    } else {
        Py_RETURN_FALSE;
    }
}

static PyMethodDef HashMethods[] = {
    {"hash_password", hash_password, METH_VARARGS, "Returns hashed password."},
    {"check_password", check_password, METH_VARARGS, "Checks if password matches hash."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef hashmodule = {
    PyModuleDef_HEAD_INIT,
    "hash_module",
    "Module for hashing passwords",
    -1,
    HashMethods
};

PyMODINIT_FUNC PyInit_hash_module(void) {
    return PyModule_Create(&hashmodule);
}
