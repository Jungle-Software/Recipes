import { useQuery, gql } from "@apollo/client";
import { View, Prompt } from "./RecipeView.styles";
import DevError from "../../../components/DevError/DevError";
import { SELECT_RECIPE_PROMPT } from "../../../constants";
import LoadingMessage from "../../../components/LoadingMessage/LoadingMessage";

export const RECIPE_BY_ID_QUERY = gql`
    query RecipeById($id: ID!) {
        recipeById(id: $id) {
            title
            description
            categories{
                name
            }
            servings
            prepTime
            cookTime
            instructions{
                title
                text
                subInstructions {
                    text
                }
            }
            ingredients{
                ingredient{
                    name
                    allergens{
                        type
                    }
                }
                unit
                quantity
            }
            additionalNotes
            dateUpdated
            dateCreated
        }
    }
`;

type Props = {
  recipeId: number
}

const RecipeView = (props: Props) => {
  const recipeId = props.recipeId;
  const { data, loading, error } = useQuery(RECIPE_BY_ID_QUERY, {
    variables: { id: recipeId },
  });

  if (recipeId === 0) return <Prompt id="select-recipe-prompt">{SELECT_RECIPE_PROMPT}</Prompt>;
  if (loading) return <LoadingMessage />;
  if (error) return <DevError message={error.message}/>;


    const instructions = data.recipeById.instructions.map((instruction:any, i:any) => { {/* TODO CHANGE ANY FOR A BETTER TYPE */}
        const subInstructions = instruction.subInstructions.map((subInstruction:any, j:any) => {
            return <div id={subInstruction.id}>
                {i+1}.{j+1}. {subInstruction.text}
            </div>
        })
        return <div id={instruction.id}>
            {i+1}. {instruction.title} {instruction.text} <br />
            <p style={{paddingLeft:"1em"}}>{subInstructions}</p>
        </div>
    })

    const ingredients = data.recipeById.ingredients.map((ingredientItem:any) => {
        const allergens = ingredientItem.ingredient[0].allergens.map((allergen:any) => {
            return allergen.type
        })

        return <div id={ingredientItem.id}>
            {ingredientItem.quantity} {ingredientItem.unit} {ingredientItem.ingredient[0].name} {allergens}
        </div>
    })

    const categories = data.recipeById.categories.map((category:any) => {
        return category.name+", "
    })

  return (
      <View id="recipe-view">
          {data.recipeById.title}
          <br />
          <br />

          <div className="Informations">
              Description: {data.recipeById.description} <br />
              Categories: {categories} <br />
              Servings: {data.recipeById.servings}  <br />
              Preparation time: {data.recipeById.prepTime} minutes <br />
              Cooking time: {data.recipeById.cookTime} minutes <br />
          </div>

          <br/>

          <div className="Ingredients">
              Ingredients: <br />
              <div style={{paddingLeft:"1em"}}>
                  {ingredients}
              </div>
          </div>

          <br/>

          <div className="Instructions">
              Instructions: <br />
              <div style={{paddingLeft:"1em"}}>
                  {instructions}
              </div>
          </div>

          <br/>
          <div className="ExtraInformation">
              Additional Notes: {data.recipeById.additionalNotes} <br />
              Date last updated: {data.recipeById.dateUpdated} <br />
              Date created: {data.recipeById.dateCreated} <br/>
          </div>

        </View>
  );
};

export default RecipeView;
