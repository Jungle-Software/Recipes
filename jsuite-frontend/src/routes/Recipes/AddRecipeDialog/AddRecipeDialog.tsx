import { gql, useMutation } from "@apollo/client";
import { useState } from "react";
import { Form, Modal } from "react-bootstrap";
import DevError from "../../../components/DevError/DevError";
import { Button } from "./AddRecipeDialog.styles";

// TODO implement this
export const ADD_RECIPE_MUTATION = gql`
  mutation AddRecipe($input: RecipeInput!) {
    createRecipe(input: $input){
      recipe {
        title,
        description,
        portionSize,
        prepTime,
        cookTime,
        ingredients,
        instructions,
        additionalNotes,
        nutritionalInfo 
      }
    }
  }
`;

type Props = {
    show: boolean
    hide: Function
    handleCreate: Function
}

const AddRecipeDialog = (props: Props) => {
    const [formState, setFormState] = useState({
        // TODO use some better way to initialize this (find a way to initialize empty model, and define a model)
        title: "TITLE",
        description: "DESCRIPTION",
        portionSize: 4,
        prepTime: 30,
        cookTime: 30,
        ingredients: "INGREDIENTS",
        instructions: "INSTRUCTIONS",
        additionalNotes: "ADDITIONALNOTES",
        nutritionalInfo: "NUTRITIONALINFO"
    })

    const [addRecipe, { data, loading, error }] = useMutation(ADD_RECIPE_MUTATION, {
        variables: {
            input: {
                title: formState.title,
                description: formState.description,
                portionSize: formState.portionSize,
                prepTime: formState.prepTime,
                cookTime: formState.cookTime,
                ingredients: formState.ingredients,
                instructions: formState.instructions,
                additionalNotes: formState.additionalNotes,
                nutritionalInfo: formState.nutritionalInfo
            }
        },
        onCompleted() {
            props.handleCreate()
        },
        onError() { }
    });

    if (loading) return <div>Adding...</div>;
    if (error) return <DevError message={error.message}></DevError>;
    // TODO maybe show a snackbar or something on fail/success (if data) (part of UI task)

    return (
        <Modal show={props.show} onHide={() => { props.hide() }}>
            {/* TODO do we want a static backdrop or no? (prevents from clicking outside) https://react-bootstrap.github.io/components/modal/*/}
            <Form onSubmit={(e) => {
                e.preventDefault();
                addRecipe();
            }}
            >
                <Form.Label>Title</Form.Label>
                <Form.Control
                    value={formState.title}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            title: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Enter recipe title"
                />

                <Form.Label>Description</Form.Label>
                <Form.Control
                    value={formState.description}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            description: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Enter a description"
                />

                <Form.Label>Portion Size</Form.Label>
                <Form.Control
                    value={formState.portionSize}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            portionSize: parseInt(e.target.value) // TODO find clean way to not have errors when value is empty (NaN)
                        })
                    }
                    type="number"
                    placeholder="How many servings?"
                />

                <Form.Label>Prep Time</Form.Label>
                <Form.Control
                    value={formState.prepTime}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            prepTime: parseInt(e.target.value)
                        })
                    }
                    type="number"
                    placeholder="How long to prepare? (minutes)"
                />

                <Form.Label>Cook Time</Form.Label>
                <Form.Control
                    value={formState.cookTime}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            cookTime: parseInt(e.target.value)
                        })
                    }
                    type="number"
                    placeholder="How long to cook? (minutes)"
                />

                <Form.Label>Ingredients</Form.Label>
                <Form.Control
                    value={formState.ingredients}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            ingredients: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Gonna be redone."
                />

                <Form.Label>Instructions</Form.Label>
                <Form.Control
                    value={formState.instructions}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            instructions: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Gonna be redone."
                />

                <Form.Label>Additional Notes</Form.Label>
                <Form.Control
                    value={formState.additionalNotes}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            additionalNotes: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Gonna be nuked."
                />

                <Form.Label>Nutritional Info</Form.Label>
                <Form.Control
                    value={formState.nutritionalInfo}
                    onChange={(e) =>
                        setFormState({
                            ...formState,
                            nutritionalInfo: e.target.value
                        })
                    }
                    type="text"
                    placeholder="Gonna be redone"
                />
                <Button type="submit">
                    Submit
                </Button>
            </Form>
        </Modal>
    )
}

export default AddRecipeDialog;